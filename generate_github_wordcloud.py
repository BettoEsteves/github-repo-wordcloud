#!/usr/bin/env python3
"""
CloudWordsGenerator

Gera uma nuvem de palavras a partir dos nomes, descrições, tópicos e linguagens dos repositórios públicos de qualquer usuário do GitHub.

Autores:
- Jose Alberto Esteves
- GitHub Copilot
"""
import argparse
import requests
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def fetch_repos(user):
    url = f"https://api.github.com/users/{user}/repos?per_page=100"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def fetch_topics(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/topics"
    resp = requests.get(url, headers={"Accept": "application/vnd.github.mercy-preview+json"})
    if resp.status_code == 200:
        return resp.json().get('names', [])
    return []

def extract_keywords(repos, user):
    keywords = []
    for repo in repos:
        if repo.get('name'): keywords.extend(repo['name'].split('-'))
        if repo.get('description'): keywords.extend(repo['description'].split())
        if repo.get('language'): keywords.append(repo['language'])
        topics = fetch_topics(user, repo['name'])
        keywords.extend(topics)
    # Limpar e normalizar
    keywords = [k.strip().replace('_', ' ').replace('-', ' ') for k in keywords if k and len(k) > 1]
    return ' '.join(keywords)

def generate_wordcloud(text, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        colormap='viridis',
        relative_scaling=0.5,
        min_font_size=10
    ).generate(text)
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"✅ Word Cloud gerada com sucesso em: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Gere uma word cloud dos repositórios públicos de um usuário do GitHub.")
    parser.add_argument('--user', required=True, help='Nome do usuário do GitHub')
    args = parser.parse_args()
    repos = fetch_repos(args.user)
    text = extract_keywords(repos, args.user)
    generate_wordcloud(text, f'wordcloud/wordcloud.png')

if __name__ == "__main__":
    main()
