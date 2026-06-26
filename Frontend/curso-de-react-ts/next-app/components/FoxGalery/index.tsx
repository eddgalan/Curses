'use client';

import { useEffect, useState } from "react";
import { RandomFox } from "@/components/FoxGalery/RandomFox";

export function FoxGallery() {
    const [images, setImages] = useState<string[]>([]);

    useEffect(() => {
        const random = () => Math.floor(Math.random() * 123) + 1;

        setImages([
            `https://randomfox.ca/images/${random()}.jpg`,
            `https://randomfox.ca/images/${random()}.jpg`,
            `https://randomfox.ca/images/${random()}.jpg`,
            `https://randomfox.ca/images/${random()}.jpg`,
        ]);
    }, []);

    return (
        <>
            {images.map((image, index) => (
                <div key={index} className="p-4">
                    <RandomFox imageUrl={image} />
                </div>
            ))}
        </>
    );
}
