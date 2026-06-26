'use client';

import { useEffect, useState } from "react";
import { RandomFox } from "@/components/FoxGalery/RandomFox";

type ImageItem = { id: string, url: string }

export function FoxGallery() {
    const [images, setImages] = useState<Array<ImageItem>>([]);

    useEffect(() => {
        const random = () => Math.floor(Math.random() * 123) + 1;
        const generateId = () => Math.random().toString(36).substring(2, 9);

        setImages([
            {id: generateId(), url: `https://randomfox.ca/images/${ random() }.jpg`},
            {id: generateId(), url: `https://randomfox.ca/images/${ random() }.jpg`},
            {id: generateId(), url: `https://randomfox.ca/images/${ random() }.jpg`},
            {id: generateId(), url: `https://randomfox.ca/images/${ random() }.jpg`},
        ]);
    }, []);

    return (
        <>
            {images.map(({ id, url }) => (
                <div key={ id } className="p-4">
                    <RandomFox imageUrl={ url } />
                </div>
            ))}
        </>
    );
}
