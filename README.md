import { render } from 'github-buttons'

// export function render(anchor: HTMLAnchorElement, callback: (el: HTMLElement) => void): void;
render(anchor, function (el) {
  anchor.parentNode.replaceChild(el, anchor)
})

// export function render(options: object, callback: (el: HTMLElement) => void): void;
render(options, function (el) {
  document.body.appendChild(el) 
})
