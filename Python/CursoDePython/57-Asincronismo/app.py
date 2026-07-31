import asyncio


async def process_data(data):
    print(f"Procesando {data}")

    await asyncio.sleep(10)
    print(f"{data} procesado")
    return data * 2


async def main():
    print("Inicio de procesamiento")
    result = await process_data("archivo.txt")
    print(f"Resultado: {result}")


if __name__ == "__main__":
    asyncio.run(main())
