<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;

class Etudiant extends Model
{
    use HasFactory;

    protected $table = 'etudiants';

    // Corrigez le nom de la propriété à 'fillable'
    protected $fillable = [
        'id',
        'nom',
        'prenom',
        'email',
        'password'
    ];
}
