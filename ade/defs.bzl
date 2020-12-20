
def _deploy_ade_impl(ctx):
    deploy = ctx.executable._deploy
    out = ctx.actions.declare_file(ctx.label.name + ".json")
    ctx.actions.run(
        executable = deploy,
        arguments = [ctx.label.name, out.path],
        inputs = [],
        tools = [deploy],
        outputs = [ out ],
        progress_message = "Deploying {} ...".format(ctx.label.name),
        use_default_shell_env = True,
    )

deploy_ade = rule(
    implementation = _deploy_ade_impl,
    attrs = {
        "_deploy": attr.label(
            default = Label("//ade:deploy"),
            allow_files = True,
            executable = True,
            cfg = "exec",
        ),
    },
)
