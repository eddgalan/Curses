'use client';

import { useState } from "react";
import type { MouseEventHandler } from "react";
import { LazyImage } from "@/components/FoxGallery/LazyImage";

type ImageItem = { id: string, url: string }

export function FoxGallery() {
    const [images, setImages] = useState<Array<ImageItem>>([]);

    const random = () => Math.floor(Math.random() * 123) + 1;
    const generateId = () => Math.random().toString(36).substring(2, 9);

    /**
     * Adds a new random fox image to the gallery.
     *
     * RandomFox provides images from 1 to 123, so the generated URL must stay within that range.
     */
    const addNewFox: MouseEventHandler<HTMLButtonElement> = (): void => {
        const newImage: ImageItem = {
            id: generateId(),
            url: `https://randomfox.ca/images/${ random() }.jpg`
        };
        setImages(prev => [...prev, newImage]);
    };

    return (
        <>
            <button className="bg-amber-300 border-2 rounded-sm p-4 m-2 hover:bg-amber-500"
                    onClick={ addNewFox }
            >
                Add new fox</button>
            {images.map(({ id, url }, index) => (
                <div key={ id } className="p-4">
                    <LazyImage
                        src={ url }
                        alt="Fox"
                        width="350"
                        className="h-auto rounded-lg bg-gray-300"
                        onClick={() => console.log('Clicked!')}
                        onLazyLoad={(img) => {
                            console.log(`Image #${index + 1} cargada. Nodo:`, img);
                        }}
                    />
                </div>
            ))}
        </>
    );
}
