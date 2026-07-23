from typing import Dict, Any
from pathlib import Path

from agents.base import BaseAgent


class VisionAgent(BaseAgent):
    """
    Vision Agent

    Отговаря за обработката на изображения.
    Засега само валидира и подготвя файловете.
    По-късно ще използва OCR и AI Vision.
    """

    name = "vision"

    tools = [
        "vision",
        "image",
        "ocr",
        "screen",
        "screenshot"
    ]

    SUPPORTED_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".bmp",
        ".webp"
    }

    def can_handle(self, action: Dict[str, Any]) -> bool:
        return action.get("agent", "").lower() == "vision"

    def execute(self, action: Dict[str, Any]) -> Dict[str, Any]:

        image_path = action.get("image")

        if not image_path:
            return {
                "success": False,
                "error": "Не е подадено изображение."
            }

        image = Path(image_path)

        if not image.exists():
            return {
                "success": False,
                "error": "Файлът не съществува."
            }

        if image.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            return {
                "success": False,
                "error": "Неподдържан файлов формат."
            }

        return {
            "success": True,
            "message": "Изображението е успешно заредено.",
            "file": str(image),
            "extension": image.suffix.lower(),
            "size": image.stat().st_size
        }

    def status(self):

        return {
            "supported_formats": sorted(self.SUPPORTED_EXTENSIONS)
        }


vision_agent = VisionAgent()
