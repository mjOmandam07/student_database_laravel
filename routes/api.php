<?php

use App\Http\Controllers\CollegeController;
use App\Http\Controllers\CourseController;
use App\Http\Controllers\DepartmentController;
use App\Http\Controllers\StudentController;
use App\Models\College;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});


Route::get('colleges', [CollegeController::class, 'index']);
Route::get('students', [StudentController::class, 'show']);
Route::get('get_students/{filter}', [StudentController::class, 'filter']);
Route::get('search_students/{params}', [StudentController::class, 'search']);

Route::group(['prefix' => 'dynamic'], function () {
    Route::get('department/{college_code}',  [DepartmentController::class, 'index']);
    Route::get('courses/{deptNo}',  [CourseController::class, 'index']);
});

Route::group(['prefix' => 'editDynamic'], function () {
    Route::get('course/{course_code}',  [CourseController::class, 'show']);
    Route::get('department/{id}',  [DepartmentController::class, 'show']);
    Route::get('college/{college_code}',  [CollegeController::class, 'show']);
});

Route::post('add_student', [StudentController::class, 'store']);
Route::delete('delete_student/{id}', [StudentController::class, 'destroy']);
Route::put('update_student/{id}', [StudentController::class, 'update']);