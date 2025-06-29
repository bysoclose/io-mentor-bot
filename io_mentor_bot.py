import sys
import asyncio
from dotenv import load_dotenv
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QSpacerItem,
    QMessageBox, QComboBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from iointel import Agent, Workflow
import nest_asyncio
from datetime import datetime

nest_asyncio.apply()
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

# Çeviriler
translations = {
    "en": {
        "title": "IO.NET Assistant",
        "input_placeholder": "Write your prompt...",
        "send_button": "Send",
        "clear_button": "Clear Chat",
        "social_label": "Social Media:",
        "loading": "⏳ Loading...",
        "copy_success": "Copied to clipboard!",
        "content_warning": "This content contains hate speech or harassment!",
        "agent_descriptions": {
            "Summary Agent": "Transforms large amounts of text into short, meaningful summaries. Ideal for reports and executive overviews.",
            "Sentiment Analysis Agent": "Evaluates emotions in the text as positive, negative, or neutral. Great for feedback analysis.",
            "Named Entity Recognizer": "Extracts key entities such as names, dates, organizations, and locations from text.",
            "Custom Agent": "Versatile agent for automation, data analysis, and custom tasks.",
            "Moderation Agent": "Detects harmful language and ensures content safety.",
            "Classification Agent": "Categorizes, labels, and structures content accurately.",
            "Translation Agent": "Translates content while preserving context and tone."
        },
        "agent_examples": {
            "Summary Agent": "Example: Summarize this article: 'Artificial intelligence is transforming industries...'",
            "Sentiment Analysis Agent": "Example: Analyze sentiment of: 'I love the new IO.NET interface!'",
            "Named Entity Recognizer": "Example: Extract entities from: 'Barack Obama was born in Hawaii on August 4, 1961.'",
            "Custom Agent": "Example: What are some creative ways to use decentralized AI in education?",
            "Moderation Agent": "Example: Check if this content is appropriate: 'You are such an idiot!'",
            "Classification Agent": "Example: Classify this story: 'In a galaxy far away, robots gained consciousness.'",
            "Translation Agent": "Example: Translate to French: 'Hello, how are you today?'"
        },
        "agent_features": {
            "Summary Agent": "Condenses lengthy texts into concise summaries, preserving key points for quick understanding.",
            "Sentiment Analysis Agent": "Analyzes text to determine emotional tone, ideal for customer feedback or social media analysis.",
            "Named Entity Recognizer": "Identifies and extracts entities like names, dates, and locations for structured data extraction.",
            "Custom Agent": "Handles diverse tasks like automation and data analysis, tailored to specific user needs.",
            "Moderation Agent": "Detects harmful language (hate speech, harassment, etc.) and assigns safety scores to ensure content safety.",
            "Classification Agent": "Classifies text into predefined categories, useful for organizing or labeling content.",
            "Translation Agent": "Translates text accurately across languages while maintaining context and tone."
        }
    },
    "tr": {
        "title": "IO.NET Asistanı",
        "input_placeholder": "Sorunuzu yazın...",
        "send_button": "Gönder",
        "clear_button": "Sohbeti Temizle",
        "social_label": "Sosyal Medya:",
        "loading": "⏳ Yükleniyor...",
        "copy_success": "Panoya kopyalandı!",
        "content_warning": "Bu içerik nefret söylemi veya taciz içeriyor!",
        "agent_descriptions": {
            "Summary Agent": "Büyük miktarda metni kısa ve anlamlı özetlere dönüştürür. Raporlar ve yönetici özetleri için ideal.",
            "Sentiment Analysis Agent": "Metindeki duyguları pozitif, negatif veya nötr olarak değerlendirir. Geri bildirim analizi için harika.",
            "Named Entity Recognizer": "Metinden isim, tarih, organizasyon ve konum gibi anahtar varlıkları çıkarır.",
            "Custom Agent": "Otomasyon, veri analizi ve özel görevler için çok yönlü bir ajan.",
            "Moderation Agent": "Zararlı dili tespit eder ve içeriğin güvenliğini sağlar.",
            "Classification Agent": "İçeriği doğru bir şekilde sınıflandırır, etiketler ve düzenler.",
            "Translation Agent": "Metni bağlam ve tonu koruyarak farklı dillere çevirir."
        },
        "agent_examples": {
            "Summary Agent": "Örnek: Bu makaleyi özetle: 'Yapay zeka endüstrileri dönüştürüyor...'",
            "Sentiment Analysis Agent": "Örnek: Şu metnin duygusunu analiz et: 'Yeni IO.NET arayüzünü çok sevdim!'",
            "Named Entity Recognizer": "Örnek: Şu metinden varlıkları çıkar: 'Barack Obama, 4 Ağustos 1961'de Hawaii'de doğdu.'",
            "Custom Agent": "Örnek: Merkezi olmayan yapay zekanın eğitimde yaratıcı kullanım yolları nelerdir?",
            "Moderation Agent": "Örnek: Bu içeriğin uygunluğunu kontrol et: 'Sen tam bir aptalsın!'",
            "Classification Agent": "Örnek: Bu hikayeyi sınıflandır: 'Uzak bir galakside, robotlar bilinç kazandı.'",
            "Translation Agent": "Örnek: Fransızcaya çevir: 'Merhaba, bugün nasılsın?'"
        },
        "agent_features": {
            "Summary Agent": "Uzun metinleri kısa ve öz özetlere dönüştürür, temel noktaları koruyarak hızlı anlaşılmasını sağlar.",
            "Sentiment Analysis Agent": "Metnin duygusal tonunu analiz eder, müşteri geri bildirimleri veya sosyal medya analizi için idealdir.",
            "Named Entity Recognizer": "İsim, tarih ve konum gibi varlıkları tanımlar ve çıkarır, yapılandırılmış veri elde etmek için kullanılır.",
            "Custom Agent": "Otomasyon ve veri analizi gibi çeşitli görevleri yerine getirir, kullanıcı ihtiyaçlarına özelleştirilir.",
            "Moderation Agent": "Metindeki zararlı dili (nefret söylemi, taciz, vb.) tespit eder ve güvenlik puanları verir.",
            "Classification Agent": "Metni önceden tanımlı kategorilere sınıflandırır, içerik düzenleme ve etiketleme için kullanışlıdır.",
            "Translation Agent": "Metni farklı dillere doğru bir şekilde çevirir, bağlam ve tonu korur."
        }
    },
    "de": {
        "title": "IO.NET Assistent",
        "input_placeholder": "Geben Sie Ihre Anfrage ein...",
        "send_button": "Senden",
        "clear_button": "Chat löschen",
        "social_label": "Soziale Medien:",
        "loading": "⏳ Lädt...",
        "copy_success": "In die Zwischenablage kopiert!",
        "content_warning": "Dieser Inhalt enthält Hassrede oder Belästigung!",
        "agent_descriptions": {
            "Summary Agent": "Verwandelt große Textmengen in kurze, aussagekräftige Zusammenfassungen. Ideal für Berichte und Managementübersichten.",
            "Sentiment Analysis Agent": "Bewertet Emotionen im Text als positiv, negativ oder neutral. Ideal für Feedback-Analysen.",
            "Named Entity Recognizer": "Extrahiert wichtige Entitäten wie Namen, Daten, Organisationen und Orte aus Texten.",
            "Custom Agent": "Vielseitiger Agent für Automatisierung, Datenanalyse und benutzerdefinierte Aufgaben.",
            "Moderation Agent": "Erkennt schädliche Sprache und sorgt für die Sicherheit von Inhalten.",
            "Classification Agent": "Kategorisiert, labelt und strukturiert Inhalte präzise.",
            "Translation Agent": "Übersetzt Inhalte unter Beibehaltung von Kontext und Ton."
        },
        "agent_examples": {
            "Summary Agent": "Beispiel: Fassen Sie diesen Artikel zusammen: 'Künstliche Intelligenz verändert Industrien...'",
            "Sentiment Analysis Agent": "Beispiel: Analysieren Sie die Stimmung von: 'Ich liebe die neue IO.NET-Schnittstelle!'",
            "Named Entity Recognizer": "Beispiel: Entitäten extrahieren aus: 'Barack Obama wurde am 4. August 1961 in Hawaii geboren.'",
            "Custom Agent": "Beispiel: Welche kreativen Möglichkeiten gibt es, dezentrale KI in der Bildung einzusetzen?",
            "Moderation Agent": "Beispiel: Überprüfen Sie, ob dieser Inhalt angemessen ist: 'Du bist so ein Idiot!'",
            "Classification Agent": "Beispiel: Klassifizieren Sie diese Geschichte: 'In einer weit entfernten Galaxie erlangten Roboter Bewusstsein.'",
            "Translation Agent": "Beispiel: Ins Französische übersetzen: 'Hallo, wie geht es Ihnen heute?'"
        },
        "agent_features": {
            "Summary Agent": "Verdichtet lange Texte in präzise Zusammenfassungen und bewahrt wichtige Punkte für schnelles Verständnis.",
            "Sentiment Analysis Agent": "Analysiert den emotionalen Ton eines Textes, ideal für Kundenfeedback oder Social-Media-Analysen.",
            "Named Entity Recognizer": "Erkennt und extrahiert Entitäten wie Namen, Daten und Orte für strukturierte Datenextraktion.",
            "Custom Agent": "Erledigt vielfältige Aufgaben wie Automatisierung und Datenanalyse, angepasst an spezifische Nutzerbedürfnisse.",
            "Moderation Agent": "Erkennt schädliche Sprache (Hassrede, Belästigung, etc.) und vergibt Sicherheitsbewertungen.",
            "Classification Agent": "Kategorisiert Texte in vordefinierte Kategorien, nützlich für Inhaltsorganisation und -kennzeichnung.",
            "Translation Agent": "Übersetzt Texte präzise in verschiedene Sprachen und bewahrt Kontext und Ton."
        }
    }
}

# Ajanlar için görev ve talimat eşleşmesi
agent_task_mapping = {
    "Summary Agent": {
        "task": "summarize_text",
        "args": {"max_words": 50}
    },
    "Sentiment Analysis Agent": {
        "task": "sentiment",
        "args": {}
    },
    "Named Entity Recognizer": {
        "task": "extract_categorized_entities",
        "args": {}
    },
    "Custom Agent": {
        "task": "custom",
        "args": {"name": "custom-task", "objective": "", "instructions": ""}
    },
    "Moderation Agent": {
        "task": "moderation",
        "args": {"threshold": 0.5}
    },
    "Classification Agent": {
        "task": "classify",
        "args": {"classify_by": ["fact", "fiction", "sci-fi", "fantasy"]}
    },
    "Translation Agent": {
        "task": "translate_text",
        "args": {"target_language": "en"}
    }
}

async def run_workflow(user_input, selected_agent_name, current_language):
    agent_config = agent_task_mapping.get(selected_agent_name, agent_task_mapping["Custom Agent"])
    task_name = agent_config["task"]
    args = agent_config["args"].copy()
    instructions = translations[current_language]["agent_descriptions"][selected_agent_name]

    agent = Agent(
        name=selected_agent_name,
        instructions=instructions,
        model="meta-llama/Llama-3.3-70B-Instruct",
        api_key=api_key,
        base_url="https://api.intelligence.io.solutions/api/v1"
    )

    input_text = user_input
    if task_name == "translate_text":
        if "çevir" in user_input.lower() or "translate to" in user_input.lower():
            parts = user_input.split(":", 1) if ":" in user_input else user_input.split(" to ", 1)
            if len(parts) > 1:
                target_lang = parts[0].strip().lower()
                input_text = parts[1].strip()
                lang_map = {
                    "ingilizce": "en", "english": "en",
                    "fransızca": "fr", "french": "fr",
                    "ispanyolca": "es", "spanish": "es",
                    "almanca": "de", "german": "de"
                }
                args["target_language"] = lang_map.get(target_lang, "en")

    workflow = Workflow(objective=input_text, client_mode=False)

    try:
        if task_name == "summarize_text":
            result = await workflow.summarize_text(**args, agents=[agent]).run_tasks()
        elif task_name == "sentiment":
            result = await workflow.sentiment(**args, agents=[agent]).run_tasks()
        elif task_name == "extract_categorized_entities":
            result = await workflow.extract_categorized_entities(**args, agents=[agent]).run_tasks()
        elif task_name == "custom":
            args["objective"] = input_text
            args["instructions"] = instructions
            result = await workflow.custom(**args, agents=[agent]).run_tasks()
        elif task_name == "moderation":
            result = await workflow.moderation(**args, agents=[agent]).run_tasks()
        elif task_name == "classify":
            result = await workflow.classify(**args, agents=[agent]).run_tasks()
        elif task_name == "translate_text":
            result = await workflow.translate_text(**args, agents=[agent]).run_tasks()
        else:
            raise ValueError(f"Unknown task: {task_name}")
        return result["results"][task_name]
    except Exception as e:
        return f"Error: {str(e)}"

def copy_to_clipboard(text, current_language):
    app.clipboard().setText(text)
    QMessageBox.information(None, translations[current_language]["copy_success"], f"'{text}' {translations[current_language]['copy_success']}")

def on_click_copy(text, current_language):
    copy_to_clipboard(text, current_language)

class WorkerSignals(QObject):
    result_ready = pyqtSignal(str)

class Worker(QThread):
    def __init__(self, user_input, selected_agent_name, signals, current_language):
        super().__init__()
        self.user_input = user_input
        self.selected_agent_name = selected_agent_name
        self.signals = signals
        self.current_language = current_language

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(run_workflow(self.user_input, self.selected_agent_name, self.current_language))
            self.signals.result_ready.emit(str(result))
        except Exception as e:
            self.signals.result_ready.emit(f"Error: {str(e)}")
        finally:
            loop.close()

class IOAssistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_language = "en"  # Varsayılan dil İngilizce
        self.setWindowTitle(translations[self.current_language]["title"])
        self.setGeometry(100, 100, 800, 900)
        self.workers = []

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)

        self.background_label = QLabel(main_widget)
        pixmap = QPixmap("background.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.lower()

        self.title_label = QLabel(translations[self.current_language]["title"], self)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        self.layout.addWidget(self.title_label, alignment=Qt.AlignCenter)

        self.layout.addSpacerItem(QSpacerItem(20, 40))

        # Dil seçimi menüsü (sol tarafta, %40 daha büyük)
        language_widget = QWidget(self)
        language_layout = QHBoxLayout(language_widget)
        self.language_label = QLabel("Language:", self)
        self.language_label.setStyleSheet("font-size: 18px; color: white;")
        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["English", "Türkçe", "Deutsch"])
        self.language_combo.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: red; border: 3px solid white; padding: 5px; font-size: 18px;")
        self.language_combo.setMinimumWidth(120)  # %40 daha büyük (200 -> 280)
        self.language_combo.setMinimumHeight(42)  # %40 daha büyük (30 -> 42)
        self.language_combo.currentTextChanged.connect(self.change_language)
        language_layout.addWidget(self.language_label)
        language_layout.addWidget(self.language_combo)
        language_layout.addStretch()
        self.layout.addWidget(language_widget, alignment=Qt.AlignLeft)

        # Girdi alanı (ajan seçimi %40 daha büyük)
        input_widget = QWidget(self)
        input_layout = QHBoxLayout(input_widget)
        self.agent_combo = QComboBox(self)
        self.agent_combo.addItems(translations[self.current_language]["agent_descriptions"].keys())
        self.agent_combo.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: red; border: 3px solid white; padding: 5px; font-size: 18px;")
        self.agent_combo.setMinimumWidth(280)  # %40 daha büyük (200 -> 280)
        self.agent_combo.setMinimumHeight(42)  # %40 daha büyük (30 -> 42)
        self.agent_combo.currentTextChanged.connect(self.update_example_label)
        self.input_entry = QLineEdit(self)
        self.input_entry.setPlaceholderText(translations[self.current_language]["input_placeholder"])
        self.input_entry.setStyleSheet("background-color: rgba(0, 0, 0, 0); font-size: 26px; color: white; border: 3px solid white; padding: 5px;")
        self.input_entry.setMinimumWidth(840)
        self.input_entry.setMinimumHeight(100)
        self.input_entry.returnPressed.connect(self.on_submit)
        self.submit_btn = QPushButton(translations[self.current_language]["send_button"], self)
        self.submit_btn.setStyleSheet("background-color: #162447; color: red; padding: 5px;")
        self.submit_btn.clicked.connect(self.on_submit)
        input_layout.addWidget(self.agent_combo)
        input_layout.addWidget(self.input_entry)
        input_layout.addWidget(self.submit_btn)
        self.layout.addWidget(input_widget, alignment=Qt.AlignCenter)

        # Örnek ve özellik etiketleri
        self.example_label = QLabel("", self)
        self.example_label.setStyleSheet("color: lightgray; font-style: italic; font-size: 13px;")
        self.layout.addWidget(self.example_label)
        self.features_label = QLabel("", self)
        self.features_label.setStyleSheet("color: lightgray; font-style: italic; font-size: 13px;")
        self.layout.addWidget(self.features_label)

        self.loading_label = QLabel("", self)
        self.loading_label.setStyleSheet("font-size: 16px; color: orange; qproperty-alignment: AlignCenter;")
        self.layout.addWidget(self.loading_label)

        self.chat_textbox = QTextEdit(self)
        self.chat_textbox.setReadOnly(True)
        self.chat_textbox.setStyleSheet("background-color: rgba(0, 0, 0, 0); font-size: 16px; color: white; border: 3px solid white;")
        self.layout.addWidget(self.chat_textbox)

        self.output_textbox = QTextEdit(self)
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setStyleSheet("background-color: rgba(0, 0, 0, 0); font-size: 16px; color: white; border: 3px solid white;")
        self.layout.addWidget(self.output_textbox)

        self.clear_btn = QPushButton(translations[self.current_language]["clear_button"], self)
        self.clear_btn.setStyleSheet("background-color: #162447; color: white; padding: 5px;")
        self.clear_btn.clicked.connect(self.clear_chat_history)
        self.layout.addWidget(self.clear_btn, alignment=Qt.AlignCenter)

        # Sosyal medya bağlantıları (orijinal ikonlar)
        self.social_widget = QWidget(self)
        self.social_layout = QHBoxLayout(self.social_widget)
        self.social_label = QLabel(translations[self.current_language]["social_label"], self)
        self.social_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        self.social_layout.addWidget(self.social_label)

        self.social_links = [
            ("github.png", "https://github.com/bysoclose/io-mentor-bot"),
            ("discord.png", "https://discord.gg/cXN3WghNhG"),
            ("twitter.png", "https://twitter.com/bilal_ibanoglu")
        ]
        self.social_link_labels = []
        for icon_path, link in self.social_links:
            link_text = QLabel(self)
            pixmap = QPixmap(icon_path).scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            link_text.setPixmap(pixmap)
            link_text.setStyleSheet("padding: 5px;")
            link_text.setToolTip(link)
            link_text.mousePressEvent = lambda e, t=link: on_click_copy(t, self.current_language)
            self.social_layout.addWidget(link_text)
            self.social_link_labels.append(link_text)
        self.social_layout.addStretch()
        self.layout.addWidget(self.social_widget, alignment=Qt.AlignCenter)

        self.resizeEvent = self.on_resize
        self.update_example_label(self.agent_combo.currentText())

        self.show()

    def change_language(self, language):
        lang_map = {"English": "en", "Türkçe": "tr", "Deutsch": "de"}
        self.current_language = lang_map.get(language, "en")
        self.update_ui_language()

    def update_ui_language(self):
        self.setWindowTitle(translations[self.current_language]["title"])
        self.title_label.setText(translations[self.current_language]["title"])
        self.input_entry.setPlaceholderText(translations[self.current_language]["input_placeholder"])
        self.submit_btn.setText(translations[self.current_language]["send_button"])
        self.clear_btn.setText(translations[self.current_language]["clear_button"])
        self.social_label.setText(translations[self.current_language]["social_label"])
        self.agent_combo.clear()
        self.agent_combo.addItems(translations[self.current_language]["agent_descriptions"].keys())
        self.update_example_label(self.agent_combo.currentText())

    def update_example_label(self, agent_name):
        example = translations[self.current_language]["agent_examples"].get(agent_name, "")
        features = translations[self.current_language]["agent_features"].get(agent_name, "")
        self.example_label.setText(example)
        self.features_label.setText(f"Features: {features}")

    def on_resize(self, event):
        pixmap = QPixmap("background.jpg").scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def process_user_input(self, user_input):
        self.loading_label.setText(translations[self.current_language]["loading"])
        self.submit_btn.setEnabled(False)
        selected_agent_name = self.agent_combo.currentText()
        signals = WorkerSignals()
        worker = Worker(user_input, selected_agent_name, signals, self.current_language)
        worker.signals.result_ready.connect(lambda result: self.handle_result(result))
        self.workers.append(worker)
        worker.finished.connect(lambda: self.workers.remove(worker))
        worker.start()

    def handle_result(self, result):
        self.output_textbox.setText(result)
        # Moderation Agent için uyarı kontrolü
        if "'hate_speech': 1.0" in result or "'harassment': 1.0" in result:
            QMessageBox.warning(self, "Content Warning", translations[self.current_language]["content_warning"])
        self.chat_textbox.append(f"You: {self.input_entry.text().strip()}\nAgent: {result}\n")
        self.input_entry.clear()
        self.loading_label.setText("")
        self.submit_btn.setEnabled(True)

    def on_submit(self):
        user_input = self.input_entry.text().strip()
        if user_input:
            self.process_user_input(user_input)

    def clear_chat_history(self):
        self.chat_textbox.clear()
        self.output_textbox.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IOAssistant()
    sys.exit(app.exec_())
