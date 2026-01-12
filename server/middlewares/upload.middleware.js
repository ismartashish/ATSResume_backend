export const uploadMiddleware = (_, __, next) => next();
import multer from "multer";

const upload = multer({
  storage: multer.memoryStorage(), // 🚀 NOTHING SAVED
  limits: {
    fileSize: 2 * 1024 * 1024 // 2MB limit
  }
});

export default upload;
