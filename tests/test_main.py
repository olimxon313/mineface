import unittest
import cv2
import os
from mineface_project import MineFace

class TestMineFace(unittest.TestCase):
    def setUp(self):
        """Подготовка перед тестами: проверяем, есть ли тестовое изображение"""
        self.img_path = "tests/test.png"  # Убедись, что файл существует!
        if not os.path.exists(self.img_path):
            raise FileNotFoundError(f"Файл {self.img_path} не найден!")

    def test_pixelate_face(self):
        """Тестируем функцию pixelate_face()"""
        mineface = MineFace()
        img = cv2.imread(self.img_path)

        self.assertIsNotNone(img, "Ошибка: изображение не загружено!")
        
        result = mineface.pixelate_face(img)
        self.assertIsNotNone(result, "Ошибка: результат None!")
        
        # Проверяем, что размер изображения не изменился
        self.assertEqual(img.shape[:2], result.shape[:2], "Ошибка: размер изображения изменился!")

if __name__ == "__main__":
    unittest.main()
