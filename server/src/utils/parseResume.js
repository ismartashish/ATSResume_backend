export function parseResume(text) {
  const sections = {
    profile: "",
    experience: [],
    education: "",
    skills: ""
  };

  const lines = text.split("\n");

  let current = "profile";
  let job = null;

  for (let line of lines) {
    const l = line.trim();

    if (/experience/i.test(l)) {
      current = "experience";
      continue;
    }
    if (/education/i.test(l)) {
      current = "education";
      continue;
    }
    if (/skills/i.test(l)) {
      current = "skills";
      continue;
    }

    if (current === "experience") {
      if (/developer|engineer|intern/i.test(l)) {
        if (job) sections.experience.push(job);
        job = { title: l, bullets: [] };
      } else if (l.startsWith("•") || l.startsWith("-")) {
        job?.bullets.push(l.replace(/^[-•]/, "").trim());
      }
    } else {
      sections[current] += l + "\n";
    }
  }

  if (job) sections.experience.push(job);
  return sections;
}
