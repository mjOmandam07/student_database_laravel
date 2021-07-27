<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateStudentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('students', function (Blueprint $table) {
            $table->id()->autoIncrement();
            $table->timestamps();
            $table->string('id_number', 9)->unique()->nullable(false);
            $table->string('firstName', 50)->nullable(false);
            $table->string('lastName', 50)->nullable(false);
            $table->integer('yearLevel')->nullable(false);
            $table->string('gender', 10)->nullable(false);
            $table->string('course_code')->nullable();
            $table->foreign('course_code')->references('code')->on('courses')->onDelete('set null')->onUpdate('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('students');
    }
}
