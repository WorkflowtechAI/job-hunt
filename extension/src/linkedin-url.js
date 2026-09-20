// Shared between the content script and the options page.
// Loaded as a plain script in both, so it hangs one object off the global.
(function (root) {
  'use strict';

  var PREFIX = 'https://www.linkedin.com/in/';

  // Anything that is clearly not a vanity slug. LinkedIn allows unicode and
  // hyphens, so the rule is what a slug may NOT contain rather than a whitelist.
  var BAD_SLUG = /[\s/\\<>"'`]/;

  // Accepts any of these and returns the canonical profile URL:
  //   jane-q-public
  //   linkedin.com/in/jane-q-public
  //   https://www.linkedin.com/in/jane-q-public/
  //   https://linkedin.com/in/jane-q-public?originalSubdomain=mx
  // Returns '' when there is nothing usable, so callers never store junk.
  function normalize(raw) {
    var s = String(raw == null ? '' : raw).trim();
    if (!s) return '';

    var slug;
    var m = s.match(/linkedin\.com\/in\/([^/?#\s]+)/i);
    if (m) {
      slug = m[1];
    } else if (/linkedin\.com/i.test(s)) {
      // A LinkedIn URL that is not a /in/ profile (a company page, a feed post).
      return '';
    } else {
      slug = s.replace(/^\/+|\/+$/g, '').split(/[?#]/)[0];
    }

    try {
      slug = decodeURIComponent(slug);
    } catch (e) {
      /* leave it as typed */
    }
    slug = slug.replace(/^\/+|\/+$/g, '');

    if (!slug || BAD_SLUG.test(slug)) return '';
    return PREFIX + slug;
  }

  root.LinkedInUrl = { PREFIX: PREFIX, normalize: normalize };
})(typeof globalThis !== 'undefined' ? globalThis : this);
