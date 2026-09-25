<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;

class LoginController extends Controller
{
    /**
     * Handles user login by validating credentials and generating an authentication token on success.
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function login(Request $request): JsonResponse
    {
        $this->validateLogin($request);

        if (Auth::attempt($request->only('email', 'password'))) {
            return response()->json([
                'token' => Auth::user()->createToken($request->name)->plainTextToken,
                'message' => 'Logged in successfully'
            ]);
        }

        return response()->json([
            'message' => 'Unauthorized'
        ], 401);
    }

    /**
     * Validates the login request by ensuring the required fields are provided and meet the specified criteria.
     *
     * @param Request $request
     * @return array
     */
    protected function validateLogin(Request $request): array
    {
        return $request->validate([
            'email' => 'required|email',
            'password' => 'required',
            'name' => 'required',
        ]);
    }
}
