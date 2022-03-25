let calendar;

function popupUpdateModal({num}) {
    const div = document.createElement('div');
    div.id = 'calPopup';
    div.innerHTML = `<div>
        <button onclick="location='/list/update/${num}/'" id="edit" class="btn btn-info">
            edit
        </button>
        <form action="/list/delete/${num}/" method="post">
            <button id="delete" class="btn btn-danger">
                delete
            </button>
        </form>
    </div>`;
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
    document.getElementById('edit').addEventListener('click', handleEdit);
    document.getElementById('delete').addEventListener('click', handleDelete);

    function handleEdit(e) {
        setTimeout(() => {
            div?.remove();
        }, 100);
        removeEventListener('click', handleEdit);
    }

    function handleDelete(e) {
        setTimeout(() => {
            div?.remove();
        }, 100);
        removeEventListener('click', handleDelete);
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
      
        if(typeof parseInt(last_url) == 'number')
        axios({
            method: 'get',
            url: `/calendar_list/${last_url}/`,
            data: {}
        }).then(function (response) {
            datas = response.data;
            datas = datas.map(x=>{
                x.fields['num'] = x.pk;
                x.fields['start'] = x.fields['start_date'];
                delete x.fields['start_date'];
                x.fields['end'] = x.fields['end_date'];
                delete x.fields['end_date'];
                return x.fields;
            });

            // 이벤트 추가 - fullcalendar
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
                // mousedown
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
                if (!document.querySelector('#calPopup'))
                    popupUpdateModal(info.event._def.extendedProps);
                // function send(data) {
                //     info.event.setProp('title', data)
                // }
            },
            eventChange: function (info) {
                // console.log(info)
            },
            eventMouseEnter: function(info) {
                const {category, coworker, regdate, room_num, schedule, title, updates, user_num} = info.event._def.extendedProps;
                const {startStr:start, endStr:end} = info.event;

                // document.querySelector('#calendar').insertAdjacentHTML('beforeend', `<div class="position-fixed top-50 popover show" role="tooltip" id="popover267739" style="top: ${top-y}px; left: ${left}px; display: block;"><div class="arrow" style="left: 50%;"></div><h3 class="popover-title"><div class="popoverTitleCalendar" style="background: rgb(151, 117, 250); color: rgb(255, 255, 255);">${title}</div></h3><div class="popover-content"><div class="popoverInfoCalendar"><p><strong>등록자:</strong> ${coworker.split(',').map(x=>`<span class="badge bg-info">${x}</span>`).join('')}</p><p><strong>구분:</strong> ${category}</p><p><strong>시간:</strong> ${start} ~ ${end}</p><div class="popoverDescCalendar"><strong>설명:</strong>${schedule}</div></div></div></div>`)
            },
            eventMouseLeave: function (info) {
                document.querySelectorAll('.popover').forEach(e=>e.remove());
            }
        });

        setTimeout(() => {
            calendar.render();
        }, 100);
    }
});