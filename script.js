'use strict';
// Tüm dinamik metinler textContent ile yazılır; kullanıcı girdisi HTML yapılmaz.
document.documentElement.classList.add('js');
const root = document.documentElement;
const themeButton = document.querySelector('.theme-toggle');
function applyTheme(theme) {
  root.dataset.theme = theme;
  themeButton?.setAttribute('aria-pressed', String(theme === 'dark'));
  themeButton?.setAttribute('aria-label', theme === 'dark' ? 'Açık temayı aç' : 'Karanlık temayı aç');
}
let initialTheme = 'light';
try { if (localStorage.getItem('jt-theme') === 'dark') initialTheme = 'dark'; } catch { /* Depolama engelliyse varsayılan tema kullanılır. */ }
applyTheme(initialTheme);
themeButton?.addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try { localStorage.setItem('jt-theme', next); } catch { /* Tema yine değişir. */ }
});

const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
function closeMenu() { menuButton?.setAttribute('aria-expanded','false'); navigation?.removeAttribute('data-open'); }
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  if (open) {
    navigation.dataset.open = 'true';
    // Menü DOM'da düğmeden önce. Odağı taşımazsak Tab bağlantıları atlar.
    navigation.querySelector('a')?.focus();
  } else navigation.removeAttribute('data-open');
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') { closeMenu(); menuButton.focus(); }
});
navigation?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });

const projectCards = [...document.querySelectorAll('#project-list .project-card')];
const search = document.querySelector('#project-search');
let category = 'Tümü';
function filterProjects() {
  const query = (search?.value || '').trim().toLocaleLowerCase('tr-TR');
  let visible = 0;
  projectCards.forEach(card => {
    const matches = (category === 'Tümü' || card.dataset.category === category) && card.textContent.toLocaleLowerCase('tr-TR').includes(query);
    card.hidden = !matches;
    if (matches) visible++;
  });
  const count = document.querySelector('#project-count');
  if (count) count.textContent = `${visible} çalışma gösteriliyor.`;
  const empty = document.querySelector('#no-results');
  if (empty) empty.hidden = visible > 0;
}
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  category = button.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
  filterProjects();
}));
search?.addEventListener('input', filterProjects);

const form = document.querySelector('#contact-form');
if (form) {
  const name = document.querySelector('#contact-name');
  const email = document.querySelector('#contact-email');
  const message = document.querySelector('#contact-message');
  const preview = document.querySelector('#message-preview');
  const status = document.querySelector('#form-status');
  const errors = { name: document.querySelector('#name-error'), email: document.querySelector('#email-error'), message: document.querySelector('#message-error') };
  function setError(field, text) { field.setAttribute('aria-invalid', String(Boolean(text))); errors[field.name].textContent = text; }
  [name,email,message].forEach(field => field.addEventListener('input', () => {
    setError(field,''); preview.hidden = true; status.textContent = '';
    document.querySelector('#message-counter').textContent = `${message.value.length} / 1000`;
  }));
  form.addEventListener('submit', event => {
    event.preventDefault();
    const problems = [
      [name, name.value.trim().length < 2 || name.value.trim().length > 60 ? 'Adınızı 2–60 karakter arasında yazın.' : ''],
      [email, !email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim()) || email.value.length > 254 ? 'Geçerli bir e-posta yazın; örnek: ad@ornek.com.' : ''],
      [message, message.value.trim().length < 10 || message.value.length > 1000 ? 'Mesajınız 10–1000 karakter arasında olmalı.' : '']
    ];
    problems.forEach(([field,text]) => setError(field,text));
    const first = problems.find(([,text]) => text);
    if (first) { preview.hidden = true; status.textContent = 'Lütfen işaretli alanları kontrol edin.'; first[0].focus(); return; }
    document.querySelector('#message-text').textContent = `Ad: ${name.value.trim()}\nE-posta: ${email.value.trim()}\n\n${message.value.trim()}`;
    preview.hidden = false;
    status.textContent = 'Mesaj taslağı hazır. Henüz gönderilmedi; metni kopyalayabilirsiniz.';
  });
  document.querySelector('#copy-message')?.addEventListener('click', async () => {
    const text = document.querySelector('#message-text').textContent;
    try { await navigator.clipboard.writeText(text); status.textContent = 'Taslak panoya kopyalandı. Bu işlem mesajı göndermez.'; }
    catch { status.textContent = 'Panoya erişilemedi. Aşağıdaki taslağı seçerek elle kopyalayabilirsiniz.'; }
  });
}

// Son Sinyal: üç sona ulaşan küçük bir karar ağacı.
const storyNodes = {
  baslangic: {step:'BAŞLANGIÇ',title:'İstasyonda yalnız değilsin.',text:'Kontrol odasındaki radyo aynı sinyali tekrarlıyor. Koridorun sonunda ise zayıf bir ışık var. Nereye gideceksin?',choices:[['Radyoyu incele →','radyo'],['Koridora ilerle →','koridor']]},
  radyo: {step:'KARAR / 01',title:'Sinyal sana cevap veriyor.',text:'Ses, istasyonu terk etmeni söylüyor. Koordinatlar açık ama sinyalin kaynağı belirsiz. Ne yapacaksın?',choices:[['Koordinatları takip et →','kurtulus'],['Sinyalin kaynağını araştır →','arsiv']]},
  koridor: {step:'KARAR / 01',title:'Işığın ardında bir kapı var.',text:'Kapının ekranında iki seçenek görünüyor: acil çıkış ve istasyon arşivi. Hangisini açacaksın?',choices:[['Acil çıkışı aç →','yalniz'],['Arşive gir →','arsiv']]},
  kurtulus: {step:'SON / 01',title:'Bir ışık daha.',text:'Koordinatlar seni çalışan bir kurtarma aracına götürüyor. Sinyali göndereni göremiyorsun, ama yalnız olmadığını biliyorsun.',choices:[]},
  arsiv: {step:'SON / 02',title:'Kendi sesin.',text:'Arşivde eski bir kayıt buluyorsun. Radyodaki ses sana ait. İstasyonun hikâyesi bitti sandığın yerde yeniden başlıyor.',choices:[]},
  yalniz: {step:'SON / 03',title:'Sessiz bir çıkış.',text:'Kapı açılıyor. İstasyonun dışına adım atıyorsun. Sinyal kesiliyor; verdiğin kararın cevabını yolun devamında arayacaksın.',choices:[]}
};
function showStory(key, focus = true) {
  const node = storyNodes[key]; if (!node) return;
  document.querySelector('#story-step').textContent = node.step;
  const title = document.querySelector('#story-title'); title.textContent = node.title;
  document.querySelector('#story-text').textContent = node.text;
  const choices = document.querySelector('#story-choices'); choices.replaceChildren();
  node.choices.forEach(([text,next]) => { const button = document.createElement('button'); button.type='button'; button.textContent=text; button.dataset.story=next; choices.append(button); });
  document.querySelector('#story-status').textContent = node.choices.length ? '' : 'Hikâye tamamlandı. Farklı bir son için baştan başlayabilirsiniz.';
  if (focus) title.focus();
}
document.querySelector('#story-choices')?.addEventListener('click', event => { const button=event.target.closest('[data-story]'); if (button) showStory(button.dataset.story); });
document.querySelector('#story-reset')?.addEventListener('click', () => showStory('baslangic'));

const balance = document.querySelector('#balance-form');
balance?.addEventListener('submit', event => {
  event.preventDefault();
  const fields = ['damage','interval','health'].map(id=>document.getElementById(id));
  const invalid = fields.find(field => !field.checkValidity() || !field.value.trim());
  fields.forEach(field=>field.setAttribute('aria-invalid',String(field===invalid)));
  if (invalid) { document.querySelector('#balance-error').textContent='Değerleri belirtilen aralıklarda girin. Hasar ve can tam sayı olmalı.'; document.querySelector('#balance-result').hidden=true; invalid.focus(); return; }
  const [damage, interval, health] = fields.map(field=>Number(field.value));
  const hits = Math.ceil(health/damage);
  const format = value => new Intl.NumberFormat('tr-TR',{maximumFractionDigits:2}).format(value);
  document.querySelector('#dps').textContent=format(damage/interval);
  document.querySelector('#hits').textContent=format(hits);
  document.querySelector('#ttk').textContent=format((hits-1)*interval)+' sn';
  document.querySelector('#balance-error').textContent='';document.querySelector('#balance-result').hidden=false;
});
const stages = [
  ['Karşılama','Oyuncu güvenli bir alanda hareket eder. Çıkış yönü görünürdür; henüz süre veya düşman baskısı yoktur.'],
  ['Öğrenme','Tek ve alçak bir engel, zıplama hareketini denetir. Başarısızlığın bedeli düşüktür; oyuncu hemen yeniden deneyebilir.'],
  ['Deneme','İki engel arka arkaya gelir. Oyuncu aynı hareketi farklı mesafelerde kullanır; öğrendiği kuralı kendi başına uygular.'],
  ['Ustalık','Daha uzun bir geçiş, önceki iki fikri birleştirir. Çıkış görünür kalır ve başarılı hareketin ardından güvenli bir dinlenme alanı gelir.']
];
document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{
  const [name,description]=stages[Number(button.dataset.stage)];
  document.querySelector('#stage-name').textContent=name;document.querySelector('#stage-description').textContent=description;
  document.querySelectorAll('[data-stage]').forEach(other=>other.setAttribute('aria-pressed',String(other===button)));
}));
