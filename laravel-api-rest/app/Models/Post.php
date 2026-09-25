<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;


class Post extends Model
{
    /** @use HasFactory<\Database\Factories\PostFactory> */
    use HasFactory;

    /**
     * @return string
     */
    public function getExcerptAttribute(): string
    {
        return substr($this->content, 0, 100);
    }


    /**
     * @return string
     */
    public function getPublishedAtAttribute(): string
    {
        return $this->created_at->diffForHumans();
    }

    /**
     * @return BelongsTo
     */
    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
