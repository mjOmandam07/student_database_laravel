<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class StudentRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
            'firstName'  => 'required',
            'lastName'  => 'required',
            'gender' => 'required',
            'id_number' => 'required|regex : /^[0-9]{4}-[0-9]{4}$/',
            'yearLevel' => 'required',
            'college' => 'required',
            'department' => 'required',
            'course_code' => 'required'
        ];
    }
}
