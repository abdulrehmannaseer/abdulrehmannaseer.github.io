/* Read the scheduled Scholar snapshot; never query Google Scholar in a visitor's browser. */
(function () {
  'use strict';
  var container = document.getElementById('scholar-citations');
  if (!container) return;
  var scholarId = 'ZTuS-yUAAAAJ';
  var cacheKey = 'scholar-citations-' + scholarId;
  var url = 'https://raw.githubusercontent.com/abdulrehmannaseer/abdulrehmannaseer.github.io/google-scholar-stats/gs_data.json';
  var displayedDate = container.getAttribute('data-updated') || '';

  function valid(data) {
    return data && data.scholar_id === scholarId && Number.isInteger(data.citations)
      && data.citations >= 0 && /^\d{4}-\d{2}-\d{2}$/.test(data.updated)
      && !Number.isNaN(Date.parse(data.updated));
  }
  function display(data) {
    if (!valid(data)) return false;
    if (data.updated < displayedDate) return false;
    displayedDate = data.updated;
    container.querySelector('[data-citation-count]').textContent = data.citations.toLocaleString('en-AU');
    container.querySelector('[data-citation-label]').textContent = data.citations === 1 ? 'citation' : 'citations';
    container.hidden = false;
    return true;
  }
  try { display(JSON.parse(localStorage.getItem(cacheKey))); } catch (error) { /* Cache is optional. */ }
  var controller = new AbortController();
  var timeout = window.setTimeout(function () { controller.abort(); }, 6000);
  fetch(url, { signal: controller.signal, cache: 'no-cache' })
    .then(function (response) {
      if (!response.ok) throw new Error('Citation snapshot unavailable');
      return response.json();
    })
    .then(function (data) {
      if (display(data)) {
        try { localStorage.setItem(cacheKey, JSON.stringify(data)); } catch (error) { /* Storage may be disabled. */ }
      }
    })
    .catch(function () {
      // A checked-in snapshot also works before the first scheduled refresh.
      return fetch(container.getAttribute('data-snapshot-url'), { cache: 'no-cache' })
        .then(function (response) {
          if (!response.ok) throw new Error('Saved citation snapshot unavailable');
          return response.json();
        })
        .then(display)
        .catch(function () { /* The server-rendered verified count remains visible. */ });
    })
    .finally(function () { window.clearTimeout(timeout); });
})();
