<?php

namespace App\Http\Controllers;

use App\Models\student;
use Illuminate\Http\Request;
use App\Http\Requests\StudentRequest;

class StudentController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return view('student.index');
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StudentRequest $studentRequest, student $student)
    {  
        // if ($studentRequest->validated()){
        //     $student = $student::create($studentRequest->all());
        // };
        $studentRequest->validated();
        $studentData = student::create($studentRequest->all('id_number', 'firstName', 'lastName', 'yearLevel', 'gender', 'course_code'));
        return response()->json(['message'=> 'student added', 'data' => $studentData]);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\student  $student
     * @return \Illuminate\Http\Response
     */
    public function show(student $student)
    {
        $students = student::all();
        return $students;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\student  $student
     * @return \Illuminate\Http\Response
     */
    public function filter($code)
    {

        $data = student::Join('courses', 'courses.code','students.course_code')
        ->join('departments', 'departments.dept_id', 'courses.deptNo')
        ->join('colleges', 'colleges.code', 'departments.college_code')
        ->where('colleges.code', $code)->get();

        return $data;
    }

    public function search($params)
    {

        $data = student::where('firstName', 'like', '%'.$params.'%')
        ->orWhere('LastName', 'like', '%'.$params.'%')
        ->orWhere('id_number', 'like', '%'.$params.'%')
        ->orWhere('course_code', 'like', '%'.$params.'%')
        ->get();

        return $data;
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\student  $student
     * @return \Illuminate\Http\Response
     */
    public function update(StudentRequest $studentRequest, student $student, $id)
    {
        $studentRequest->validated();
        $studentData = student::where('id_number',$id)->update($studentRequest->all('id_number', 'firstName', 'lastName', 'yearLevel', 'gender', 'course_code'));
        return response()->json(['message'=> 'student added', 'data' => $studentData]);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\student  $student
     * @return \Illuminate\Http\Response
     */
    public function destroy(student $student, $id)
    {
        return student::where('id_number', $id)->delete();
    }
}
