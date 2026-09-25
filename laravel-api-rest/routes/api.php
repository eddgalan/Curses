<?php

use App\Http\Controllers\Api\V1\PostController;
use Illuminate\Support\Facades\Route;

Route::apiResource('v1/posts', PostController::class)
    ->only(['index', 'show']);
