import * as pdfjsLib from "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.5.136/pdf.min.mjs";

console.log("=================================");
console.log("PDF.js Loaded");
console.log(pdfjsLib);
console.log("=================================");

const pdfContainer = document.querySelector(".pdf-container");

if (pdfContainer) {
    console.log("PDF URL:", pdfContainer.dataset.pdfUrl);
}