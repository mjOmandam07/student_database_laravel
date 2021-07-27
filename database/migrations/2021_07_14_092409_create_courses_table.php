<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCoursesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('courses', function (Blueprint $table) {
            $table->id()->autoIncrement();
            $table->timestamps();
            $table->string('code', 20)->unique();
            $table->string('name');
            $table->integer('deptNo')->nullable();
            $table->string('college_code',20)->nullable();
            $table->foreign('deptNo')->references('dept_id')->on('departments')->onDelete('set null')->onUpdate('cascade');
            $table->foreign('college_code')->references('college_code')->on('departments')->onDelete('set null')->onUpdate('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('courses');
    }
}
