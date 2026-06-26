import { JSX } from "react";
import { FoxGallery } from "@/components/FoxGallery";

export default function Home(): JSX.Element {
    return (
        <main className="flex flex-col items-center">
            <h1 className="text-3xl font-bold underline">Fox Gallery</h1>
            <FoxGallery/>
        </main>
    );
}
