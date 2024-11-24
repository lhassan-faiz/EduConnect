<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Resources\EtudiantResource;
use App\Models\Etudiant;
use Illuminate\Http\Request;

class EtudiantController extends Controller
{
    public function index(){
        $etudiants = Etudiant::get();
        if($etudiants){
            return EtudiantResource::collection($etudiants);
   
        }
        else
        {
            return response()->json(['message'=> 'No record available'], 200);
        }

    }
    public function store(Request $request){
        $request->validate([
            'nom' => 'required|string|max:255',
            'prenom' => 'required|string|max:255',
            'email' => 'required|string|max:255',
            'password' => 'required|string|max:255',
        ]);
        $etudiant = Etudiant::create([
            'nom' => $request->nom,
            'prenom' => $request->prenom,
            'email' => $request->email,
            'password' => $request->password,
        ]);
        return response()->json([
            'message' => 'Etudiant created Seccessfully',
            'data' => new EtudiantResource($etudiant)
        ]);
    }
    public function show(Etudiant $etudiant){


        return new EtudiantResource($etudiant);
        
    }


    public function update(Request $request, Etudiant $etudiant)
{ 
        $request->validate([
            'nom' => 'required|string|max:255',
            'prenom' => 'required|string|max:255',
            'email' => 'required|string|max:255',
            'password' => 'required|string|max:255',
        ]);
        $etudiant -> update([
            'nom' => $request->nom,
            'prenom' => $request->prenom,
            'email' => $request->email,
            'password' => $request->password,
        ]);
        return response()->json([
            'message' => 'Etudiant Updated Seccessfully',
            'data' => new EtudiantResource($etudiant)
        ]);
    
}
    public function destroy(Etudiant $etudiant)
    {
       $etudiant->delete();

       return response()->json([
        'message' => 'Etudiant Deleted Seccessfully',
    ]);

    }
}
