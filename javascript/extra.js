// Makes the header logo link to the external Etherion Designs website
document.addEventListener("DOMContentLoaded", function () {
  var logo = document.querySelector(".md-header__button.md-logo");
  if (logo) {
    logo.setAttribute("href", "https://www.etheriondesigns.com");
    logo.setAttribute("target", "_blank");
  }
});


// Wrap standalone "PRO" text in a glowing purple span
function wrapProText(root) {
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode: function (node) {
      if (!/\bPRO\b/.test(node.nodeValue)) return NodeFilter.FILTER_REJECT;
      if (node.parentElement.closest(".pro-glow, script, style, code, pre")) {
        return NodeFilter.FILTER_REJECT;
      }
      return NodeFilter.FILTER_ACCEPT;
    },
  });

  const nodes = [];
  let n;
  while ((n = walker.nextNode())) nodes.push(n);

  nodes.forEach(function (node) {
    const parts = node.nodeValue.split(/(\bPRO\b)/);
    if (parts.length === 1) return;
    const frag = document.createDocumentFragment();
    parts.forEach(function (part) {
      if (part === "PRO") {
        const span = document.createElement("span");
        span.className = "pro-glow";
        span.textContent = part;
        frag.appendChild(span);
      } else if (part) {
        frag.appendChild(document.createTextNode(part));
      }
    });
    node.parentNode.replaceChild(frag, node);
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const content = document.querySelector(".md-typeset");
  if (content) wrapProText(content);

  const navLinks = document.querySelectorAll(".md-nav__link");
  navLinks.forEach(function (link) {
    wrapProText(link);
  });
});