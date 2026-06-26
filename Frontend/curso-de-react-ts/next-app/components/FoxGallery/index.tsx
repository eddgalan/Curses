'use client';

import { useEffect, useState } from "react";
import type { MouseEventHandler } from "react";
import { RandomFox } from "@/components/FoxGallery/RandomFox";

type ImageItem = { id: string, url: string }

export function FoxGallery() {
    const [images, setImages] = useState<Array<ImageItem>>([]);

    const random = () => Math.floor(Math.random() * 123) + 1;
    const generateId = () => Math.random().toString(36).substring(2, 9);

    useEffect(() => {
        setImages([]);
    }, []);

    /**
     * Adds a new random fox image to the gallery.
     *
     * RandomFox provides images from 1 to 123, so the generated URL must stay within that range.
     */
    const addNewFox: MouseEventHandler<HTMLButtonElement> = (event): void => {
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
            {images.map(({ id, url }) => (
                <div key={ id } className="p-4">
                    <RandomFox imageUrl={ url } />
                </div>
            ))}
        </>
    );
}
