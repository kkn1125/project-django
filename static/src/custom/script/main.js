// window.addEventListener('click', );
const profile = document.getElementById('profile');
const relProfile = document.getElementById('relProfile');
const nickname = document.getElementById('nickname');
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