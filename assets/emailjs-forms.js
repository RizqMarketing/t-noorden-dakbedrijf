/* EmailJS Forms - Dakbedrijf 'T Noorden */
(function () {
  const PUBLIC_KEY  = '9zr1gguPfebTNpMEg';
  const SERVICE_ID  = 'service_m0nrook';
  const TEMPLATE_ID = 'template_n1y3yxa';

  if (typeof emailjs === 'undefined') {
    console.error('[EmailJS] SDK niet geladen. Controleer of de CDN script is toegevoegd.');
    return;
  }
  emailjs.init({ publicKey: PUBLIC_KEY });

  function collect(form) {
    const get = (n) => {
      const el = form.querySelector('[name="' + n + '"]');
      return el ? (el.value || '').trim() : '';
    };
    return {
      voornaam:      get('voornaam'),
      achternaam:    get('achternaam'),
      telefoon:      get('telefoon'),
      email:         get('email'),
      postcode_stad: get('postcode_stad'),
      dienst:        get('dienst'),
      bericht:       get('bericht'),
      form_type:     form.dataset.form || 'onbekend',
      pagina:        document.title + ' (' + window.location.pathname + ')',
      verzonden_op:  new Date().toLocaleString('nl-NL', { timeZone: 'Europe/Amsterdam' })
    };
  }

  function showSuccess(form, btn) {
    const originalText = btn.dataset.originalText || btn.textContent;
    btn.dataset.originalText = originalText;
    const span = btn.querySelector('.hf-btn-text');
    if (span) span.textContent = '✓ Aanvraag Verzonden!';
    else btn.textContent = '✓ Aanvraag Verzonden!';
    btn.style.background = '#16a34a';
    btn.disabled = true;
    setTimeout(function () {
      if (span) span.textContent = originalText;
      else btn.textContent = originalText;
      btn.style.background = '';
      btn.disabled = false;
      form.reset();
      if (form.dataset.form === 'popup' && typeof closePopup === 'function') closePopup();
    }, 3500);
  }

  function showError(btn, msg) {
    const span = btn.querySelector('.hf-btn-text');
    if (span) span.textContent = '✗ Fout - probeer opnieuw';
    else btn.textContent = '✗ Fout - probeer opnieuw';
    btn.style.background = '#dc2626';
    btn.disabled = false;
    console.error('[EmailJS]', msg);
  }

  function handleSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const btn = form.querySelector('button[type="submit"]');
    if (!btn) return;

    const originalText = btn.querySelector('.hf-btn-text')
      ? btn.querySelector('.hf-btn-text').textContent
      : btn.textContent;
    btn.dataset.originalText = originalText;

    const span = btn.querySelector('.hf-btn-text');
    if (span) span.textContent = 'Bezig met verzenden...';
    else btn.textContent = 'Bezig met verzenden...';
    btn.disabled = true;

    const params = collect(form);

    emailjs.send(SERVICE_ID, TEMPLATE_ID, params)
      .then(function () { showSuccess(form, btn); })
      .catch(function (err) { showError(btn, err); });
  }

  function init() {
    const forms = document.querySelectorAll('form[data-form]');
    forms.forEach(function (f) {
      f.removeAttribute('onsubmit');
      f.addEventListener('submit', handleSubmit);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
