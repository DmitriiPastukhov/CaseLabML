import joblib
import os
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
import numpy as np


model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
vectorizer_path = os.path.join(settings.BASE_DIR, 'vectorizer.pkl')
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def classify_review(text):
    global model, vectorizer
    X = vectorizer.transform([text])
    prediction = model.predict(X)
    probability = model.predict_proba(X)
    rating = int(np.round(probability[0][1] * 10))
    sentiment = 'positive' if prediction == 1 else 'negative'
    return rating, sentiment

def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.rating, review.sentiment = classify_review(review.text)
            
            # Отладочный вывод перед сохранением
            print(f'Saving review with rating: {review.rating}, sentiment: {review.sentiment}')
            review.save()
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def review_success(request):
    # Получаем последний добавленный отзыв
    last_review = Review.objects.latest('id')
    
    # Передаем его в шаблон
    return render(request, 'reviews/review_success.html', {
        'review': last_review
    })