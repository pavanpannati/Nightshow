const video=document.getElementById('video')
const icon=document.getElementById('mute')
function mute(){
  if (video.muted){
    video.muted=false;
    muteIcon.classList.remove('bi-volume-mute')
    muteIcon.classList.add('bi-volume-up');
  }else{
    video.muted=true;
    muteIcon.classList.remove('bi-volume-up')
    muteIcon.classList.add('bi-volume-mute');
  }
}