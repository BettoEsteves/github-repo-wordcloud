<!--
🚫 REGRA ABSOLUTA: O projeto é multiplataforma, mas o agente (Copilot) só pode criar, modificar ou versionar arquivos no ambiente Windows. Nunca gravar nada no Linux.
-->

# CloudWordsGenerator

Gere uma nuvem de palavras automaticamente a partir dos nomes, descrições, tópicos e linguagens dos repositórios públicos de qualquer usuário do GitHub.

## Como funciona

- Busca todos os repositórios públicos de um usuário do GitHub via API
- Extrai palavras-chave dos campos: nome, descrição, tópicos e linguagem
- Gera uma word cloud visual (imagem) com as palavras mais frequentes
- Salva a imagem em `wordcloud/wordcloud.png`

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/BettoEsteves/CloudWordsGenerator.git
   cd CloudWordsGenerator
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Execute o script principal informando o nome do usuário do GitHub:

```sh
python generate_github_wordcloud.py --user <usuario_github>
```

Exemplo:
```sh
python generate_github_wordcloud.py --user octocat
```

A imagem será salva em `wordcloud/wordcloud.png`.

## Exemplo de resultado

<img src="wordcloud/wordcloud.png" alt="WordCloud" width="100%">

## Licença

MIT License

## Autores
- Jose Alberto Esteves
- GitHub Copilot
