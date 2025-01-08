import os
from conan import ConanFile
from conan.tools.files import copy

class GamingNetworkSockets(ConanFile):
    settings = "os", "build_type"
    name = "gamenetworkingsockets"
    version = "1.4.0"

    def requirements(self):
        self.requires( "openssl/3.2.0")
        self.requires("protobuf/5.27.0")

    def generate(self):

        # Copy the Conan package dependencies the build folder
        for dep in self.dependencies.values():
            build_path = os.path.join(self.build_folder, "build", "conan_installed", dep.ref.name)
            copy(self, "*.*", dep.cpp_info.includedir, os.path.join(build_path, os.path.basename(dep.cpp_info.includedir)))
            copy(self, "*.*", dep.cpp_info.libdir, os.path.join(build_path, os.path.basename(dep.cpp_info.libdir)))
            copy(self, "*.*", dep.cpp_info.bindir, os.path.join(build_path, os.path.basename(dep.cpp_info.bindir)))

    def layout(self):
        self.folders.build = os.path.join( ".." )
        self.folders.source = self.folders.build
        self.cpp.includedirs = ["include"]
        
        osSubDir = "win.x86_64.vc142.mt"
        if self.settings.os == "Linux":
            osSubDir = "linux.clang"
            
        buildTypeSubDir = "debug"
        if self.settings.build_type == "Release":
            buildTypeSubDir = "checked"
        
        if self.settings.os == "Windows":
            self.cpp.build.libdirs = [ 
                os.path.join( "bin", osSubDir, buildTypeSubDir ),
                os.path.join( "compiler", "vc16win64", "sdk_source_bin", buildTypeSubDir )
            ]         
        else:
            self.cpp.build.libdirs = [ 
                os.path.join( "bin", osSubDir, buildTypeSubDir )
            ]        

    def package(self):
        local_include_folder = os.path.join( self.source_folder, "include" )
        local_lib_dir = os.path.join( self.build_folder, self.cpp.build.libdirs[ 0 ] )
        copy( self, "*.h", local_include_folder, os.path.join( self.package_folder, "include" ), keep_path = True )
        copy( self, "*.lib", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        copy( self, "*.pdb", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        copy( self, "*.a", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        copy( self, "*.dll", local_lib_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )
        
        if self.settings.os == "Windows":   
            local_pdb_dir = os.path.join( self.build_folder, self.cpp.build.libdirs[ 1 ] )
            copy( self, "*.pdb", local_pdb_dir, os.path.join( self.package_folder, "lib" ), keep_path = False )

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs = [
                # TODO - fill this out once I get it building
            ]
    
        else:
            self.cpp_info.libs = [
                # TODO - fill this out once I get it building

            ]
