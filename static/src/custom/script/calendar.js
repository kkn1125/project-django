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
        calendar = new FullCalendar.Calendar(calendarEl, {
            headerToolbar: {
                left: 'prevYear,prev,next,nextYear today',
                center: 'title',
                right: 'dayGridMonth,dayGridWeek,dayGridDay'
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
            // dateClick: function (info) {
            //     console.log(this.getEvents())
            // },
            selectAllow: function (info) {
                // mousedown
                console.log('selecting')
                return true
            },
            select: function (info) {
                // mouseup
                document.querySelector('#calPopup') ?.remove();
                if (!document.querySelector('#calPopup'))
                    popupmodal({
                        title: 'no title',
                        start: info.startStr,
                        end: info.endStr
                    });
                //this.addEvent({
                //    title: 'test',
                //    start: info.startStr,
                //    end: info.endStr,
                //});
            },
            // unselect: function (ev) {
            //   
            // },
            eventClick: function (info) {
                console.log(info.event)
                if (!document.querySelector('#calPopup'))
                    popupUpdateModal({
                        title: info.event.title,
                    }, send)

                function send(data) {
                    info.event.setProp('title', data)
                }
                // info.event.setProp('title', 'wow!')
                // 내용 변경!
                console.log(info.view.type)
            },
            eventChange: function (info) {
                console.log(info)
            },
        });
        setTimeout(() => {
            calendar.render();
        }, 100);
    }
});