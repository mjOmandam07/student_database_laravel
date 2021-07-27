<?php

namespace App\Http\Controllers;

use App\Models\College;
use App\Models\User;
use Illuminate\Http\Request;


class CollegeController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $colleges = College::all();
        return $colleges;
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
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\College  $college
     * @return \Illuminate\Http\Response
     */
    public function show($college_code)
    {
        $colleges = College::where('code', $college_code)->get();
        return $colleges;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\College  $college
     * @return \Illuminate\Http\Response
     */
    public function edit(College $college)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\College  $college
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, College $college)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\College  $college
     * @return \Illuminate\Http\Response
     */
    public function destroy(College $college)
    {
        //
    }
}
