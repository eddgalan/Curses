import {JSX } from "react";
import { FoxGallery } from "@/components/FoxGalery";

export default function Home(): JSX.Element {
    return (
        <main>
            <h1 className="text-3xl font-bold underline">Hello World!</h1>
            <FoxGallery />
        </main>
    );
}
