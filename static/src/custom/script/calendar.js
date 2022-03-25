let calendar;

function popupUpdateModal(data, send) {
    const div = document.createElement('div');
    div.id = 'calPopup';
    div.innerHTML = `
    ${Object.keys(data).map(x=>`
            <div>
                <span>${x}</span>
                <input name="${x}" type="${x=='title'?'text':'datetime-local'}" value="${data[x]+(x=='title' || data[x].match(/T/g)?'':'T00:00')}">
            </div>
        `).join('')+`<div>
            <button id="add" class="btn btn-info">
                add
            </button>
        </div>`}
    `;
    div.style.cssText = `
        background-color: white;
        position: absolute;
        z-index: 10;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 1rem;
        border-radius: 1rem;
        box-shadow: 0 0 1rem 0  rgba(0,0,0,0.5);
    `;
    document.body.append(div);
    document.getElementById('add').addEventListener('click', handleAdd);

    function handleAdd(e) {
        send(document.querySelector('input[name="title"]').value);
        div ?.remove();
        removeEventListener('click', handleAdd);
    }
}

function popupmodal(attr) {
    const div = document.createElement('div');
    div.id = 'calPopup';
    div.innerHTML = `
      ${Object.keys(attr).map(x=>`
              <div>
                  <span>${x}</span>
                  <input name="${x}" type="${x=='title'?'text':'datetime-local'}" value="${attr[x]+(x=='title' || attr[x].match(/T/g)?'':'T00:00')}">
              </div>
          `).join('')+`<div>
              <button id="add" class="btn btn-info">
                  add
              </button>
          </div>`}
      `;
    div.style.cssText = `
          background-color: white;
          position: absolute;
          z-index: 10;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          padding: 1rem;
          border-radius: 1rem;
          box-shadow: 0 0 1rem 0 rgba(0,0,0,0.5);
      `;
    document.body.append(div);
    document.getElementById('add').addEventListener('click', handleAdd);

    function handleAdd(e) {
        calendar.addEvent({
            title: document.querySelector('input[name="title"]').value,
            start: document.querySelector('input[name="start"]').value,
            end: document.querySelector('input[name="end"]').value
        });
        div ?.remove();
        removeEventListener('click', handleAdd);
    }
}

window.addEventListener('mousedown', e => {
    const target = e.target;
    if (!target.closest('#calPopup')) document.querySelector('#calPopup') ?.remove();
});

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    if (calendarEl) {
        let datas;
        const last_url = location.pathname.split('/').filter(x=>x!='').pop();
        console.log(parseInt(last_url))
        if(typeof parseInt(last_url) == 'number')
        axios({
            method: 'get',
            url: `/calendar_list/${last_url}/`,
            data: {}
        }).then(function (response) {
            datas = response.data;
            console.log(datas)
            datas = datas.map(x=>{
                return {
                    title: x.fields.title,
                    start: x.fields.start_date,
                    end: x.fields.end_date,
                }
            });

            datas.forEach(e=>{
                calendar.addEvent(e);
            });
        });
        
        calendar = new FullCalendar.Calendar(calendarEl, {
            timeZone: 'Asia/Seoul',
            headerToolbar: {
                left: 'prevYear,prev,next,nextYear today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
            dayMaxEventRows: true,
            views: {
                timeGrid: {
                    dayMaxEventRows: 5
                }
            },
            themeSystem: 'standard',
            initialView: 'dayGridMonth',
            selectable: true,
            editable: true,
            navLinks: true,
            selectAllow: function (info) {
                console.log('selecting')
                return true
            },
            select: function (info) {
                document.querySelector('#calPopup') ?.remove();

                function padDate(date){
                    return date.match(/T/g)?date:date+'T'+'00:00'
                }

                if (!document.querySelector('#calPopup'))
                    location.href = `/create/?s=${padDate(info.startStr)}&e=${padDate(info.endStr)}&r_num=${location.href.split('/').pop()}`;

            },
            eventClick: function (info) {
                console.log(info.event)
                if (!document.querySelector('#calPopup'))
                    popupUpdateModal({
                        title: info.event.title,
                    }, send);
                function send(data) {
                    info.event.setProp('title', data)
                }
            },
            eventChange: function (info) {
                // console.log(info)
            },
        });

        setTimeout(() => {
            calendar.render();
        }, 100);
    }
});