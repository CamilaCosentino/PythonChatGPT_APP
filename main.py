import openai
import config
import typer
from rich import print
from rich.table import Table
"""
Webs de interés:
- Módulo OpenAI: https://github.com/openai/openai-python
- Documentación API ChatGPT: https://platform.openai.com/docs/api-reference/chat
- Typer: https://typer.tiangolo.com
- Rich: https://rich.readthedocs.io/en/stable/
"""


def main():
    openai.api_key = config.api_key
    print("[bold magenta]ChatGPT API en Python[/bold magenta]")
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Empezar una nueva conversación")
    # Contexto del asistente
    context = {"role": "system", "content": "Eres un asistente muy útil"}
    messages = [context]

    print(table)
    
    while True:
        
        content = __prompt()
        
        if content == "new":
            print("✨ Nueva conversación")
            messages = [content]
            content = __prompt()
        
        messages.append({"role": "user", "content": content})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})

        print(
            f'[bold magenta]> [/bold magenta][magenta]{response_content}[magenta]')


def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué queres hablar?")
    if prompt == "exit":
        exit = typer.confirm(
            "✋ Estás seguro? [bold red]Esta acción no se puede revertir[/bold red]")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()
        return __prompt()
    return prompt


if __name__ == "__main__":
    typer.run(main)
