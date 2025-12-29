{
  description = "Quarto development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Use "aarch64-linux" for ARM-based WSL
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [ 
          pkgs.quarto 
          # pkgs.python311 # Optional: add if you need Python/Jupyter
        ];
      };
    };
}
