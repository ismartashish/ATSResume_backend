import fs from "fs";
import * as pdfjsLib from "pdfjs-dist/legacy/build/pdf.mjs";

export const extractText = async (filePath, mimeType) => {
  // TXT fallback
  if (mimeType !== "application/pdf") {
    return fs.readFileSync(filePath, "utf-8");
  }

  const data = new Uint8Array(fs.readFileSync(filePath));
  const pdf = await pdfjsLib.getDocument({ data }).promise;

  let text = "";

  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const content = await page.getTextContent();
    text += content.items.map(item => item.str).join(" ") + " ";
  }

  return text;
};
