import cv2
import mediapipe as mp
import pygame
import random

# تنظیمات تشخیص دست با mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_drawing = mp.solutions.drawing_utils

# تنظیمات pygame برای بارش 0 و 1
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Courier', 24)
clock = pygame.time.Clock()

# ایجاد باران اعداد 0 و 1
class MatrixRain:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-100, 0)
        self.speed = random.randint(5, 15)
        self.text = random.choice(['0', '1'])
    
    def fall(self):
        self.y += self.speed
        if self.y > screen_height:
            self.reset()
        screen.blit(font.render(self.text, True, (0, 255, 0)), (self.x, self.y))

# تشخیص لایک با mediapipe
def detect_like(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]

    if thumb_tip.y < thumb_ip.y and index_tip.y > thumb_ip.y:
        return True
    return False

# پردازش تصویر دوربین و انیمیشن
def main():
    cap = cv2.VideoCapture(0)
    rain = [MatrixRain() for _ in range(100)]
    done_displayed = False

    while True:
        # خواندن تصویر از دوربین
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # پردازش تصویر برای تشخیص دست
        result = hands.process(rgb_frame)
        
        if result.multi_hand_landmarks:
            likes_detected = 0
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                if detect_like(hand_landmarks):
                    likes_detected += 1
            
            if likes_detected == 2 and not done_displayed:
                done_displayed = True
        
        # نمایش تصویر دوربین
        cv2.imshow('Camera', frame)

        # نمایش انیمیشن در صورت تشخیص لایک
        if done_displayed:
            screen.fill((0, 0, 0))
            for drop in rain:
                drop.fall()
            done_text = font.render("done", True, (0, 255, 0))
            screen.blit(done_text, (screen_width // 2 - 50, screen_height // 2))
            pygame.display.flip()
        
        # ترک برنامه
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()
