const profile = document.getElementById('id_profile');
const relProfile = document.getElementById('relProfile');
const nickname = document.getElementById('id_nickname');
const relNickname = document.getElementById('relNickname');
const unsign = document.getElementById('unsign');

if(unsign){
    unsign.addEventListener('click', e => {
        const url = unsign.getAttribute('dir');
        const form = document.createElement('form');
        form.action = url;
        form.method = 'post';
        form.hidden = true;
        const result = confirm('탈퇴하시겠습니까?');
        if(result) {
            document.body.append(form);
            form.submit();
        }
    });
}

if(relProfile) {
    profile.addEventListener('change', e => {
        const file = [...profile.files].shift();
        let names = file.name.split('.');
        let extension = names.pop();
        names = names.join('.');

        let size = file.size;
        
        if(size/1024/1000>5){
            alert('이미지 용량은 5MB를 넘을 수 없습니다.');
            profile.value = '';
            relProfile.src = `http://placehold.jp/150x150.png`;
            relProfile.setAttribute('done', 0);
        } else {
            if(!extension.match(/jpg|jpeg|png|tiff/gi)){
                alert('잘못된 파일 형식입니다. 허용하는 파일 형식은 jpg/jpeg/png/tiff 입니다.');
                profile.value = '';
                relProfile.src = `http://placehold.jp/150x150.png`;
                relProfile.setAttribute('done', 0);
            } else {
                const preview = URL.createObjectURL(file);
                relProfile.src = preview;
                relProfile.setAttribute('done', 1);
            }
        }
    });
}

if(relNickname) {
    nickname.addEventListener('input', e => {
        relNickname.textContent = nickname.value||'No Name';
    });
}

var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl, option)
});

function createToast(title='Master', msg='No Message', time=new Date(), auto=true){
    const svg = `<svg class="bd-placeholder-img rounded me-2" width="20" height="20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="#007aff"></rect></svg>`;
    const toast = document.createElement('div');
    toast.setAttribute('class', 'toast');
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    toast.setAttribute('data-bs-autohide', auto);
    toast.innerHTML = `<div class="toast-header">
    ${svg}
    <strong class="me-auto">${title}</strong>
    <small>${time.toLocaleString()}</small>
    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
    ${msg}
    </div>`;
    return toast;
}

function addToast({title, msg, time, auto}) {
    const container = document.querySelector('.toast-container');
    const toast = createToast(title, msg, time, auto);
    container.append(toast);
    showToast(toast);
}

function showToast(toastEl){
    var toast = new bootstrap.Toast(toastEl);
    toast.show();
}