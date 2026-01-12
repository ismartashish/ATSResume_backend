export const getTemplates = (_, res) => {
  res.json([
    { id: "modern", name: "Modern ATS Friendly" },
    { id: "professional", name: "Professional" },
    { id: "minimal", name: "Minimal" }
  ]);
};
