const button = document.getElementById('dar10');
const gato = document.getElementById('gato');
const canvas = document.getElementById('confetti');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let confettiArray = [];

class Confetti {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * -canvas.height;
    this.size = Math.random() * 8 + 4;
    this.speed = Math.random() * 3 + 2;
    this.color = `hsl(${Math.random()*360}, 100%, 50%)`;
  }

  update() {
    this.y += this.speed;
    if (this.y > canvas.height) {
      this.y = -10;
      this.x = Math.random() * canvas.width;
    }
  }

  draw() {
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.size, this.size);
  }
}

function createConfetti() {
  for (let i = 0; i < 150; i++) {
    confettiArray.push(new Confetti());
  }
}

function animateConfetti() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  confettiArray.forEach(c => {
    c.update();
    c.draw();
  });
  requestAnimationFrame(animateConfetti);
}
let bt = 0
button.addEventListener('click', () => {
  // Troca imagem para gato feliz
  gato.src = gato.src.replace('gatim.png', 'gatim_feliz.png');

  bt ++
  if (bt < 2){
      createConfetti();
      animateConfetti();
  }
});
