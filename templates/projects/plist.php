		<div class="row">
			<!-- container of project list -->
			<div class="shade-container">
				<table id="project_list" class="table table-bordred table-striped">
					<!-- head of the table -->
					<!-- TO DO: dynamically generate table head -->
					<thead>
						<th>Project name</th>
						<th>Dataset</th>
						<th>Project description</th>
						<th>Last modifed time</th>
						<th>Edit</th>
						<th>Delete</th>
					</thead>				
					<tbody>
						<?php if(!empty($projects)){?>
							<?php foreach($projects as $project) {
								$project_id = $project['project_id'];
								$project_name = $project['project_name'];
								$project_description = $project['project_description'];
								$post_time = $project['post_time'];
								$dataset_name = $project['dataset_name'];
								?>
								<tr value="<?php echo $project_id;?>">
									<td><?php echo $project_name;?></td>
									<td><?php echo $dataset_name;?></td>
									<td><?php echo $project_description;?></td>
									<td><?php echo $post_time;?></td>
								    <td><p><button class="btn btn-primary btn-xs plist_update" data-title="Edit" data-toggle="modal" data-target="#edit" value="<?php echo $project_id;?>"><span class="glyphicon glyphicon-pencil"></span></button></p></td>
	    							<td><p><button class="btn btn-danger btn-xs p_delete_icon" data-title="Delete" data-toggle="modal" data-target="#delete" value="<?php echo $project_id;?>"><span class="glyphicon glyphicon-trash" ></span></button></p></td>
								</tr>
							<?php } ?>
						<?php } ?>		
					</tbody>
				</table>
			</div>

			<!-- a popup to ask user to confirm the deletion -->
			<div class="modal fade" id="delete_alert" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
				<div class="modal-dialog">
					<div class="modal-content">
						<div class="modal-header">
							<button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
							<h4 class="modal-title" id="myModalLabel">Delete This Project</h4>
						</div>
						<!-- content -->
						<div class="modal-body">
							<div class="alert alert-warning"><span class="glyphicon glyphicon-warning-sign"></span> Are you sure you want to delete this Project?</div>
							<label id="p_hidden_id" style="display: none;"></label>
						</div>

						<div class="modal-footer">
							<button type="button" class="btn btn-warning" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> No</button>
							<button type="button" class="btn btn-warning plist_delete_btn"><span class="glyphicon glyphicon-ok-sign"></span> Yes</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	    
	    <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/listprocess.js"></script>
	</body>
</html>

