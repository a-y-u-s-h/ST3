import os
import shutil
import glob

def main():
  functions = [
      "std::is_eq"
    , "std::is_gt"
    , "std::is_lt"
    , "std::is_neq"
    , "std::is_pod"
    , "std::is_enum"
    , "std::is_void"
    , "std::is_array"
    , "std::is_class"
    , "std::is_const"
    , "std::is_empty"
    , "std::is_final"
    , "std::is_union"
    , "std::is_object"
    , "std::is_scalar"
    , "std::is_signed"
    , "std::is_pointer"
    , "std::is_trivial"
    , "std::is_abstract"
    , "std::is_compound"
    , "std::is_function"
    , "std::is_integral"
    , "std::is_unsigned"
    , "std::is_volatile"
    , "std::is_aggregate"
    , "std::is_base_of_v"
    , "std::is_invocable"
    , "std::is_reference"
    , "std::is_arithmetic"
    , "std::is_convertible"
    , "std::is_fundamental"
    , "std::is_polymorphic"
    , "std::is_literal_type"
    , "std::is_null_pointer"
    , "std::chrono::is_clock"
    , "std::fstream::is_open"
    , "std::ctype::do_scan_is"
    , "std::is_floating_point"
    , "std::is_member_pointer"
    , "std::wfstream::is_open"
    , "std::is_error_code_enum"
    , "std::is_standard_layout"
    , "std::wofstream::is_open"
    , "std::atomic_is_lock_free"
    , "std::ctype_byname::do_is"
    , "std::filesystem::is_fifo"
    , "std::is_lvalue_reference"
    , "std::is_rvalue_reference"
    , "std::atomic::is_lock_free"
    , "std::ctype<char>::scan_is"
    , "std::errc::is_a_directory"
    , "std::filesystem::is_empty"
    , "std::filesystem::is_other"
    , "std::filesystem::is_socket"
    , "std::is_copy_constructible"
    , "std::filesystem::is_symlink"
    , "std::is_error_condition_enum"
    , "std::atomic_int::is_lock_free"
    , "std::atomic_ref::is_lock_free"
    , "std::filesystem::is_directory"
    , "std::is_default_constructible"
    , "std::is_member_object_pointer"
    , "std::is_nothrow_constructible"
    , "std::numeric_limits::is_exact"
    , "std::atomic_bool::is_lock_free"
    , "std::atomic_long::is_lock_free"
    , "std::atomic_uint::is_lock_free"
    , "std::filesystem::is_block_file"
    , "std::numeric_limits::is_iec559"
    , "std::numeric_limits::is_modulo"
    , "std::numeric_limits::is_signed"
    , "std::atomic_llong::is_lock_free"
    , "std::atomic_schar::is_lock_free"
    , "std::atomic_short::is_lock_free"
    , "std::atomic_uchar::is_lock_free"
    , "std::atomic_ulong::is_lock_free"
  ]

  pwd = os.getcwd()
  for f in functions:
    fname = f[f.rindex("is"):]
    foldername = f[f.index("::") : f.rindex("::")].replace("<", "-").replace(">", "-")
    if "::" in foldername:
      foldername = foldername[foldername.index("::") + 2:]
      shortcut = f"{fname}".replace("_", "")
      if not os.path.exists(f"{foldername}"):
        os.makedirs(f"{foldername}")
      os.chdir(f"{foldername}")
      # `edit` : {f}
      with open(f"{fname}.sublime-snippet", "w") as file:
        file.write(f"""<snippet>
  <content><![CDATA[
{f}($0)
]]></content>
  <tabTrigger>{shortcut}</tabTrigger>
  <scope>(source.c | source.objc | source.c++ | source.objc++) - meta.preprocessor.incomplete</scope>
</snippet>
""")
      os.chdir(f"{pwd}")
    else:
      shortcut = f"{fname}".replace("_", "")
      if not os.path.exists(f"std"):
        os.makedirs(f"std")
      os.chdir(f"std")
      with open(f"{fname}.sublime-snippet", "w") as file:
        file.write(f"""<snippet>
  <content><![CDATA[
{f}($0)
]]></content>
  <tabTrigger>{shortcut}</tabTrigger>
  <scope>(source.c | source.objc | source.c++ | source.objc++) - meta.preprocessor.incomplete</scope>
</snippet>
""")
      os.chdir(pwd)

if __name__ == '__main__':
  main()