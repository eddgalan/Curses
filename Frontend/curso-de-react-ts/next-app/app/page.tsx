import { RandomFox } from "@/components/RandomFox";

export default function Home() {
    const random = (): number => Math.floor(Math.random() * 123) + 1;

    return (
        <>
            <h1>Hello World</h1>
            <RandomFox imageUrl={`https://randomfox.ca/images/${random()}.jpg`}/>
        </>
    );
}
