from drf_spectacular.openapi import AutoSchema


class SwaggerCustomAutoSchema(AutoSchema):
    def preprocess_operation(self, result, view, path, method, *args, **kwargs):
        if method.lower() == 'patch':
            return None
        return super().preprocess_operation(result, view, path, method, *args, **kwargs)
