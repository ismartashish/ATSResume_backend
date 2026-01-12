import fs from "fs";

export const readFile = (path) =>
  fs.readFileSync(path, "utf-8");
