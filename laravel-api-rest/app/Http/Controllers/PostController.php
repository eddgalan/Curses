<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;
use \Illuminate\Contracts\View\Factory;
use \Illuminate\Contracts\View\View;

class PostController extends Controller
{
    /**
     * @return Factory|View
     */
    public function index(): Factory|View
    {
        return view('index', [
            'posts' => Post::latest()->paginate(10),
        ]);
    }
}
