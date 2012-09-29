Name

    MESA_image_sRGB

Name Strings

    EGL_MESA_image_sRGB

Contact

    John Kåre Alsaker <john.kare.alsaker@gmail.com>

Status

    Proposal

Version

    Version 1, October 9, 2012

Number

    EGL Extension #not assigned

Dependencies

    EGL 1.2 or later is required.

    EGL_KHR_image_base is required.

    This extension is written against the wording of the EGL 1.2
    specification.

Overview

    This extension provides a way for applications to allocate sRGB
    or linear gamma views for EGLImage sources. This means that
    sampling from the resulting EGLImage should convert from sRGB's
    gamma into linear gamma.

IP Status

    Open-source; freely implementable.

New Tokens

    Accepted in the <attrib_list> parameter of eglCreateImageKHR:

        EGL_GAMMA_MESA				#not assigned

    Accepted as values for the EGL_GAMMA_MESA attribute:

        EGL_DEFAULT_MESA			#not assigned
        EGL_LINEAR_MESA				#not assigned
        EGL_sRGB_MESA				#not assigned

Additions to the EGL 1.2 Specification:

    Add to section 2.5.1 "EGLImage Specification" (as defined by the
    EGL_KHR_image_base specification), in the description of
    eglCreateImageKHR:

   "Attributes names accepted in <attrib_list> are shown in Table bbb

      +----------------+-------------------------+------------------+
      | Attribute      | Description             | Default Value    |
      +----------------+-------------------------+------------------+
      | EGL_GAMMA_MESA | Specifies the gamma     | EGL_DEFAULT_MESA |
      |                | view of the             |                  |
      |                | EGLImage created.       |                  |
      +----------------+-------------------------+------------------+
       Table bbb.  Legal attributes for eglCreateImageKHR
       <attrib_list> parameter

    ...

    If the value of attribute EGL_GAMMA_MESA is EGL_DEFAULT_MESA (the
    default), then the gamma view of the resulting EGLImage will be
    the same as the EGLImage source.

    If the value of attribute EGL_GAMMA_MESA is EGL_LINEAR_MESA,
    then the gamma view of the resulting EGLImage will be linear
    and no gamma conversions will be done when sampling the image
    in client APIs.

    If the value of attribute EGL_GAMMA_MESA is EGL_sRGB_MESA,
    then the gamma view of the resulting EGLImage will be an sRGB
    view and the red, green and blue color components will be
    converted from sRGB gamma to linear gamma when sampling the image
    in client APIs. This conversion should ideally take place before
    any filtering, but that is not required. The conversion from an
    sRGB gamma component, cs, to a linear gamma component, cl, is as
    follows.

            {  cs / 12.92,                 cs <= 0.04045
       cl = {
            {  ((cs + 0.055)/1.055)^2.4,   cs >  0.04045

    Assume cs is the sRGB gamma component in the range [0,1]."

    Add to the list of error conditions for eglCreateImageKHR:

      "* If the value specified in <attrib_list> for EGL_GAMMA_MESA
         is not EGL_DEFAULT_MESA, and the implementation does not
         support creating the specified gamma view, the error
         EGL_BAD_ACCESS is generated.

       * If the value specified in <attrib_list> for EGL_GAMMA_MESA
         is EGL_sRGB_MESA, and the EGLImage source does not have
         red, green and blue color components, the error
         EGL_BAD_ACCESS is generated."

Issues

    1)  Should creating multiple EGLImages from the same source
        with a different gamma view be allowed?

        RESOLVED: Yes.

        This is so applications can easily switch between using
        an sRGB and a linear gamma view for a single EGLImage
        source.

Revision History

    Version 1, October 9, 2012
        Initial draft (John Kåre Alsaker)
