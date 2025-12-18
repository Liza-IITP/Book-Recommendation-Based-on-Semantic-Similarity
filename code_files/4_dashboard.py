!pip install -q gradio
import gradio as gr
import pandas as pd
df = pd.read_csv("/content/books_with_emotions.csv")
def recommend_books(emotion, threshold):
    filtered = df[df[emotion] >= threshold]

    if filtered.empty:
        return "No books found 😔"

    results = filtered.sort_values(by=emotion, ascending=False)
    return results[["title", "authors", emotion]].head(10)
emotion_labels = list(emotion_scores.keys())

iface = gr.Interface(
    fn=recommend_books,
    inputs=[
        gr.Dropdown(choices=emotion_labels, label="Select Emotion"),
        gr.Slider(0, 1, step=0.05, label="Minimum Emotion Intensity")
    ],
    outputs=gr.Dataframe(),
    title="📚 Emotion-Aware Book Recommender",
    description="Find books based on emotional intensity extracted from descriptions"
)

iface.launch()
